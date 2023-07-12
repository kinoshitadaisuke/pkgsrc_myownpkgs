# $NetBSD$

GITHUB_PROJECT=	astroquery
DISTNAME=	0.4.6
GITHUB_TAG=     refs/tags/v${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
MASTER_SITES=   ${MASTER_SITE_GITHUB:=astropy/}
CATEGORIES=	math

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://astroquery.readthedocs.io/en/latest/
COMMENT=	Astropy coordinated Python module for querying astronomical databases
LICENSE=	modified-bsd

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-requests>=2.25.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-keyring>=21.2.1:../../security/py-keyring
DEPENDS+=	${PYPKGPREFIX}-six>=1.15.0:../../lang/py-six
DEPENDS+=	${PYPKGPREFIX}-astropy>=4.2:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-pyvo>=1.3:../../pkgsrc_myownpkgs/py-pyvo
DEPENDS+=	${PYPKGPREFIX}-astropy-helpers>=4.0.1:../../math/py-astropy-helpers

post-extract:
	${CHMOD} -R go-w ${WRKSRC}

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
