# $NetBSD$

DISTNAME=	astroquery-0.4.9
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=   ${MASTER_SITE_PYPI:=a/astroquery/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://astroquery.readthedocs.io/en/latest/
COMMENT=	Astropy coordinated Python module for querying astronomical databases
LICENSE=	modified-bsd

WRKSRC=	${WRKDIR}/${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-requests>=2.25.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-keyring>=21.2.1:../../security/py-keyring
DEPENDS+=	${PYPKGPREFIX}-six>=1.15.0:../../lang/py-six
DEPENDS+=	${PYPKGPREFIX}-astropy>=4.2:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-pyvo>=1.3:../../pkgsrc_myownpkgs/py-pyvo
#DEPENDS+=	${PYPKGPREFIX}-astropy-helpers>=4.0.1:../../pkgsrc_myownpkgs/py-astropy-helpers

post-extract:
	${CHMOD} -R go-w ${WRKSRC}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
