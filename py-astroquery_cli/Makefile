# $NetBSD$

DISTNAME=	astroquery_cli-1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astroquery_cli/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astroquery_cli/
COMMENT=	CLI for astroquery modules with autocompletion
LICENSE=	modified-bsd

# TODO: Extract dependencies from pyproject.toml

USE_PKGLOCALEDIR=	yes
USE_LANGUAGES=		# none

DEPENDS+=	${PYPKGPREFIX}-rich>=13.5.2:../../comms/py-rich
DEPENDS+=	${PYPKGPREFIX}-babel>=2.15.0:../../devel/py-babel
DEPENDS+=	${PYPKGPREFIX}-requests>=2.10.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-typer>=0.15.4:../../pkgsrc_myownpkgs/py-typer
DEPENDS+=	${PYPKGPREFIX}-astropy>=7.1.0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0.4.10:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-pyvo>=1.4.1:../../pkgsrc_myownpkgs/py-pyvo

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} aqc aqc-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
