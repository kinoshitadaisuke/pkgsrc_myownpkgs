# $NetBSD$

DISTNAME=	skyfield-data-6.0.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/skyfield-data/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/skyfield-data/
COMMENT=	data for skyfield package
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-jplephem>=0:../../pkgsrc_myownpkgs/py-jplephem
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-tox>=0:../../devel/py-tox
DEPENDS+=	${PYPKGPREFIX}-colorama>=0:../../comms/py-colorama
DEPENDS+=	${PYPKGPREFIX}-termcolor>=0:../../devel/py-termcolor
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-skyfield>=0:../../pkgsrc_myownpkgs/py-skyfield
DEPENDS+=	${PYPKGPREFIX}-mock>=0:../../devel/py-mock

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
